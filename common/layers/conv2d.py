from typing import Tuple

import jax.numpy as jnp


class Conv2DLayer:
    """Convolutional 2D layer."""
    def __init__(self, kernel_shape: Tuple[int], stride: Tuple[int], padding: int):
        self.kernel_w, self.kernel_h, self.kernel_c = kernel_shape
        self.stride_w, self.stride_h = stride
        self.padding = padding

    def forward(self, x: jnp.ndarray) -> jnp.ndarray:
        # Apply kernel
        return x
    
    def get_output_size(self, x: jnp.ndarray) -> Tuple[int]:
        input_h, input_w = x.shape[:2]
        output_h = int((input_h + 2 * padding - self.kernel_h) / self.stride_h) + 1
        output_w = int((input_w + 2 * padding - self.kernel_w) / self.stride_w) + 1
        return output_w, output_h

