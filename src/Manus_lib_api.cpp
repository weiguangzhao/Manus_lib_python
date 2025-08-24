#include <torch/extension.h>
#include <torch/serialize/tensor.h>
#include "Manus_lib.h"

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m){
    m.def("start_manus", &start_manus, "start_manus");
}
