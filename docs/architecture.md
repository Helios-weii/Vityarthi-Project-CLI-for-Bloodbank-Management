# System Architecture

```text
                     main.py
                        |
       +----------------+----------------+
       |                |                |
     Donor          Inventory         Hospital
       |                |                |
       +----------------+----------------+
                        |
                     Search
                        |
                     Report
                        |
                  File Manager
                        |
                     .dat files
```

The main file controls the menus. Each module handles one part of the project.
File Manager is used to save and load records.
