import torch
from torch.autograd import Function
import Manus_lib


if __name__ == '__main__':

    Manus_return = Manus_lib.init_manus_sdk()
    print("complete init")
    dof_num = 20
    right_hand_dof = torch.zeros(dof_num, dtype=torch.float32).contiguous() +12.0
    assert right_hand_dof.is_contiguous()
    Manus_return = Manus_lib.start_manus_sdk(right_hand_dof)

    print("complete start")
    Manus_return = Manus_lib.close_manus_sdk()
    print(right_hand_dof)