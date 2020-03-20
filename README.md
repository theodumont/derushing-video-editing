# Video logging for editing

Python script that can be used to quickly organize rushes from a video shooting session.

## 1. Installation

To use this tool, type in a shell:
```bash
cd location_of_cli
pip install -r requirements
python cli.py
```

Don't hesitate to use the `help` command to understand the different functions of the tool.

## 2. Features

To naviguate trough directories, you can use the `>> cd` command.

### 2.1. Sort by extension
To sort files by extension, type:
```bash
>> folder
```

### 2.2. Trash useless videos
To trash the videos of length shorter than `time_limit`, type:
```bash
>> trash <time_limit>
```

### 2.3. Sort by date
To sort files by date, type:
```bash
>> date
```

### 2.4. Make renaming easier
To do
