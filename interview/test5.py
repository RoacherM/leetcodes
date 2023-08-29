"""
Author: ByronVon
Date: 2023-08-25 14:59:58
FilePath: /leetcode/interview/test5.py
Description: 
"""
import torch
import torch.nn as nn


class ScaledDotProcutionAttention(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, q, k, v, masks=None, masked=1e-12):
        # inputs: [batch, n_heads, seq_len, hidden_dim]
        hidden_dim = q.size()[-1]
        scores = torch.matmul(q, k.transpose(2, 3))
        scores = scores / torch.sqrt(torch.tensor(hidden_dim)).float()

        if masks is not None:
            # masks: [batch, seq_len, seq_len]
            scores = scores.masked_fill(mask=masks.unsqueeze(1) == 0, value=masked)

        matrix = self.softmax(scores)
        output = torch.matmul(matrix, v)
        return output, matrix


class SelfAttention(nn.Module):
    def __init__(self, d_model, n_heads) -> None:
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.hidden_dim = d_model // n_heads
        assert self.hidden_dim * n_heads == d_model

        self.WQ = nn.Linear(d_model, d_model)
        self.WK = nn.Linear(d_model, d_model)
        self.WV = nn.Linear(d_model, d_model)

        self.WO = nn.Linear(d_model, d_model)

        self.attention = ScaledDotProcutionAttention()

    def forward(self, q, k, v, masks=None):
        # inputs: [batch, seq_len, d_model]
        batch_size = q.size()[0]

        q = self.WQ(q).view(batch_size, -1, self.n_heads, self.hidden_dim)
        k = self.WK(k).view(batch_size, -1, self.n_heads, self.hidden_dim)
        v = self.WV(v).view(batch_size, -1, self.n_heads, self.hidden_dim)

        q = q.transpose(1, 2)
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)

        scores, _ = self.attention(q, k, v, masks)

        scores = scores.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)
        output = self.WO(scores)
        return output


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
