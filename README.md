<h1 align="center">
  Desktop Cleaner Script 🧹
</h1>
<p>
This script automatically moves files from a choosen directory to defined subdirectories.
</p>

## Getting started

1.  **Prerequisites**
    
    Before you start, you should have Python 3 with Pip installed.
    
    Then set up a virtual environment and install the required packages inside the project.

    ```shell
    pip install -r requirements.txt
    ```

2.  **Configure your paths**

    Now you can configure your source and destination path in the *.env* file.

    ```shell
    SOURCE_DIR=/Users/youruser/Desktop
    DESTINATION_DIR=/Users/youruser/Documents
    ```
    
    You can also change the logic on how to determine different paths for each file 
    in the *get_destination* function in *functions.py*.
    

3.  **Start the script.**
    
    You can start the script manually or set up a cron job to do so.
    ```shell
    python main.py
    ```