#include <torch/extension.h>
#include <torch/serialize/tensor.h>
#include "Manus_lib.h"

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m){
    m.def("init_manus_sdk", &init_manus_sdk, "init_manus_sdk");
    m.def("start_manus_sdk", &start_manus_sdk, "start_manus_sdk");
    m.def("close_manus_sdk", &close_manus_sdk, "close_manus_sdk");
}
