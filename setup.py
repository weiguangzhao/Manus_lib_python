from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
data_files = []
data_files.append(('lib/manus', ['src/ManusSDK/lib/libManusSDK.so']))
data_files.append(('lib/manus', ['src/ManusSDK/lib/libManusSDK_Intergrated.so']))
setup(
    name='Manus_lib',
    ext_modules=[
        CUDAExtension('Manus_lib', [
            'src/Manus_lib_api.cpp',
            'src/Start_manus.cpp',
        ],  extra_compile_args={'cxx': ['-g'], 'nvcc': ['-O2']},library_dirs=['src/ManusSDK/include'],),
    ],
    cmdclass={'build_ext': BuildExtension},
    data_files=data_files,
)