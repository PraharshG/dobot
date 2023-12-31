# Installation

::: danger BEWARE (Windows only)
Driver included with <span style="font-weight: 800">DobotStudio</span> might not be sufficient for this API to work. Please install the drivers from [here](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) and reboot your computer.
:::

## Step 1: Installing the package from PyPI

::: warning
Python 3.9 or higher is required
:::

### Poetry (recommended)

```bash
poetry add dobotapi
```

### Pip

```bash
pip install dobotapi
```

## Step 2: Installing Drivers

### Linux

::: tip You are done
Linux kernel should be able to communicate with the robot without any additional drivers.
:::

### Windows

::: warning
Windows users will need to install drivers from [this](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) link
:::

## Step 3: Connecting to the robot

Please, <span style="color: orange">connect the Dobot</span> to your computer and verify that your operating system can see him. If you are using Linux, you can check this by running the following command:

### Linux

```bash
ls /dev/ttyUSB*
```

### Windows

Press `Win+X` on your keyboard and select `Device Manager`. You should see a device called `Silicon Labs`. If you see this, your drivers are <i>probably</i> installed correctly.