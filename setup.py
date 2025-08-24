from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='Manus_lib',
    ext_modules=[
        CUDAExtension('Manus_lib', [
            'src/Manus_lib_api.cpp',
            'src/Manus_lib.cpp',
        ],
    extra_compile_args={'cxx': ['-g'], 'nvcc': ['-O2']},
    libraries=['ManusSDK','ManusSDK_Integrated','ncurses',  'pthread' ],
    library_dirs=['/home/ubuntu/weiguang/project/Manus_lib/src/ManusSDK/lib'],
    extra_link_args=['-Wl,-rpath=/home/ubuntu/weiguang/project/Manus_lib/src/ManusSDK/lib'],),
    ],
    cmdclass={'build_ext': BuildExtension},
)