import torch
from torch import nn


class PerformancePredictor(nn.Module):
    def __init__(self, input_dim: int = 16) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 4),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)


class ReinforcementLearningLoop:
    def __init__(self, learning_rate: float = 1e-3) -> None:
        self.model = PerformancePredictor()
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=learning_rate)
        self.loss_fn = nn.MSELoss()

    def train_step(self, features: torch.Tensor, labels: torch.Tensor) -> float:
        self.model.train()
        self.optimizer.zero_grad()
        predictions = self.model(features)
        loss = self.loss_fn(predictions, labels)
        loss.backward()
        self.optimizer.step()
        return float(loss.detach().item())
