# AnonNifti

This project is a small primer to a full anonymization framework project. With this script, I am testing the feasibility of converting the DICOM series to a NIFTI file which carries no patient information.

This project runs on my Windows Server 2022 server.

## Dependency

- [dcm2nixx](https://github.com/rordenlab/dcm2niix), a command line tool to convert dicom files to nifti.

You need to download the exe file, and specify the path to the file in the configuration file.

## Configuration file

The `CONFIG` file is used to specify the variables for the script. The example file is presented below.

```ini
[DEFAULT]
dcm2niix_path = ./dcm2niix/dcm2niix.exe
input_dir = ./testDCM/
output_dir = ./output/
list_path = tesList.csv
```

`dcm2niix_path` points to the `dcm2niix.exe` executable; `input_dir` is where all studies are located. `output_dir` is the place to generate the nifti files. The `list_path` variable points to the list of anonymization lookup table.

## CSV file

A file that specifies the folder name containing the study and its anonymized name. The first line of the file (header) shall not be changed.

```csv
RealName,AnonName
FDG0123,T001
FDG2345,T002
FDG3456,T003
```

## Rights and permissions

This is too simple, and I claim no copyright.
