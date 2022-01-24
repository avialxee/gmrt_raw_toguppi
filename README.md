# gmrt_raw_toguppi
To read gmrt raw voltages file of GWB to convert to guppi raw

# Usage
```bash
$ gmrt_raw_toguppi [-h] [-f FILENAME] [-c CHUNK] [-hdr HEADER] [-hf HEADER_FILE] [-hfo HEADER_FILE_OUTPUT]

    To read gmrt raw voltages file of GWB to convert to guppi raw

    optional arguments:
    -h, --help            show this help message and exit
    -f FILENAME, --filename FILENAME
                        Input filename for conversion to guppiraw.
    -c CHUNK, --chunk CHUNK
                        Input chunk size to read the desired chunk of byte.
    -hdr HEADER, --header HEADER
                        Input header to inject to the raw file.
    -hf HEADER_FILE, --header-file HEADER_FILE
                        Input header from path to inject to the raw file.
    -hfo HEADER_FILE_OUTPUT, --header-file-output HEADER_FILE_OUTPUT
                        output header from path to inject to the raw file.
```

NOTE
------

- using # in `hinput.txt` will ignore the entire field.
- change the first line to the path of your environment.