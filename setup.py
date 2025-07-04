from setuptools import Extension, setup
import platform
import os

system = platform.system()


def get_version(rel_path):
    version_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), rel_path)
    with open(version_file, encoding='utf-8') as f:
        for line in f.readlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]


if system == 'Windows':
    setup(
        name='cv2_enumerate_cameras',
        description='Enumerate / List / Find / Detect / Search index for opencv VideoCapture.',
        version=get_version('cv2_enumerate_cameras/__init__.py'),
        package_dir={"": "."},
        packages=["cv2_enumerate_cameras"],
        ext_modules=[
            Extension(
                name="cv2_enumerate_cameras._windows_backend",
                sources=["cv2_enumerate_cameras/_windows_backend.cpp"],
                py_limited_api=True,
                define_macros=[("Py_LIMITED_API", "0x03020000")]
            )
        ]
    )


if system == 'Linux':
    setup(
        name='cv2_enumerate_cameras',
        description='Enumerate / List / Find / Detect / Search index for opencv VideoCapture.',
        version=get_version('cv2_enumerate_cameras/__init__.py'),
        package_dir={"": "."},
        packages=["cv2_enumerate_cameras"],
        extras_require={
            'linuxpy': ["linuxpy"]
        },
        ext_modules=[]
    )

if system == 'Darwin':
    setup(
        name='cv2_enumerate_cameras',
        description='Enumerate / List / Find / Detect / Search index for opencv VideoCapture.',
        version=get_version('cv2_enumerate_cameras/__init__.py'),
        package_dir={"": "."},
        packages=["cv2_enumerate_cameras"],
        install_requires=[
            "pyobjc-framework-AVFoundation",
        ],
        ext_modules=[]
    )