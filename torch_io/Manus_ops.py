import torch
from torch.autograd import Function
import Manus_lib


if __name__ == '__main__':
    dof_num = 20
    right_hand_dof = torch.ones(dof_num, dtype=torch.float32).contiguous()
    assert right_hand_dof.is_contiguous()

    init_return_code = Manus_lib.init_manus_sdk() #开启SDK
    strat_return_code = Manus_lib.start_manus_sdk(right_hand_dof) # 获取当前帧数据到变量right_hand_dof
    close_return_code = Manus_lib.close_manus_sdk() #关闭SDK
