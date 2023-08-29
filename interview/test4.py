"""
Author: ByronVon
Date: 2023-08-21 15:27:15
FilePath: /leetcode/interview/test4.py
Description: 
"""

import torch
import torch.nn as nn


class ScaledDotProductionAttention(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, q, k, v, masks=None, maksed=1e-12):
        # inputs: [batch, n_heads, seq_len, hidden_dim]
        hidden_dim = q.size()[-1]

        scores = torch.matmul(
            q, k.transpose(-2, -1)
        )  # [batch, n_heads, seq_len, seq_len]

        scores = scores / torch.sqrt(torch.tensor(hidden_dim)).float()

        if masks is not None:
            # [batch, seq_len, seq_len]->[batch, 1, seq_len, seq_len]
            scores = scores.masked_fill(masks.unsqueeze(1) == 0, -maksed)

        attention_matrix = self.softmax(scores)

        output = torch.matmul(scores, v)
        return output, attention_matrix


class SelfAttention(nn.Module):
    def __init__(self, d_model, num_heads) -> None:
        super().__init__()

        self.d_model = d_model
        self.num_heads = num_heads
        self.hidden_dim = d_model // num_heads

        self.attn = ScaledDotProductionAttention()
        self.q = nn.Linear(d_model, d_model)
        self.k = nn.Linear(d_model, d_model)
        self.v = nn.Linear(d_model, d_model)

        self.fc = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, masks=None):
        # [batch, seq_len, d_model]

        batch_size = q.size()[0]

        # W(Q),W(K),W(V)->split to n_heads, [batch, seq_len, num_heads, hidden_dim]
        q = self.q(q).view(batch_size, -1, self.num_heads, self.hidden_dim)
        k = self.k(k).view(batch_size, -1, self.num_heads, self.hidden_dim)
        v = self.v(v).view(batch_size, -1, self.num_heads, self.hidden_dim)

        q = q.transpose(1, 2)  # [batch, num_heads, seq_len, hidden_dim]
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)

        scores, attn_matrix = self.attn(q, k, v, masks)

        # concat heads->[batch, seq_len, d_model]
        scores = scores.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)
        output = self.fc(scores)

        return output, attn_matrix


if __name__ == "__main__":
    batch_size = 2
    seq_len = 5
    d_model = 20
    num_heads = 4

    q = torch.rand((batch_size, seq_len, d_model))
    k = torch.rand((batch_size, seq_len, d_model))
    v = torch.rand((batch_size, seq_len, d_model))

    masks = torch.randint(0, 2, (batch_size, seq_len, seq_len))
    print(masks)

    attention_layer = SelfAttention(d_model, num_heads)

    output, _ = attention_layer(q, k, v, masks)

    print(output.shape)
    print(_)
