import torch
from torch.autograd import Function
import Manus_lib


if __name__ == '__main__':
    Manus_return = Manus_lib.init_manus_sdk()
    print("complete init")
    Manus_return = Manus_lib.start_manus_sdk()
    print("complete start")
    Manus_return = Manus_lib.close_manus_sdk()