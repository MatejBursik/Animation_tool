# Animation compiling tool

A command line program which is going to compile your frames of an animation into an video. Because it is an Python program, the command  makes its current working directory where the act.py file is located.

## Prerequisite

- frames of the animation should be numerically labeled from 1
- install python [(link)](https://www.python.org/downloads/)
- install dependencies (`pip install -r requirements.txt`)

## Arguments

List of arguments available for the command

#### Mandatory

| Argument | Description | Example |
| -------- | ------- | ------- |
| `--name` | name of the output video file | `python act.py --name example` |

#### Optional

| Argument | Description | Example | Default |
| -------- | ------- | ------- | ------- |
| `--fps` | set fps (frames per second) | `python act.py --name example --fps 25` | 30 |
| `--img` | specify the source image file type (png, jpeg, tiff) | `python act.py --name example --img jpeg` | png |
| `--path` | specify the directory of the images | `python act.py --name example --path images` | current working directory |

## Test

In this repository, I provide a set of 45 images to test if it is running correctly. To test it, run command `python act.py --name test --path test` in the cloned repository. It should generate a test.mp4 animation of a dot moving around.
