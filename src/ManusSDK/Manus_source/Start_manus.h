#include "ClientLogging.hpp"
#include "SDKClient.hpp"
#include <torch/serialize/tensor.h>
#include <ATen/cuda/CUDAContext.h>
int init_manus_sdk();
float start_manus_sdk(at::Tensor right_hand_dof_tensor);
int close_manus_sdk();