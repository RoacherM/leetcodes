"""
Author: ByronVon
Date: 2023-08-09 16:12:54
FilePath: /leetcode/面试/test2.py
Description: 
"""
"""
Author: ByronVon
Date: 2023-08-09 16:12:54
FilePath: /leetcode/面试/test2.py
Description: 
"""
# 用torch实现self-attention

import torch.nn as nn


class ScaledDotProductionAttention(nn.Module):
    def __init__(self):
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, q, k, v, mask):
        # 只要保证tensor的维度一样即可
        # 若QKV不一致，则用head控制维度
        batch, head, max_len, d_tensor = k.size()

        k = k.transpose(2, 3)
        d_k = d_model**0.5

        # 计算Q和K的转置
        score = q @ k / d_k  # [batch, head, max_len, max_len]

        if mask is not None:
            score = score.masked_fill(mask == 0, -100)
        score = self.softmax(score)
        # 和V进行相乘
        v = score @ v
        return v
