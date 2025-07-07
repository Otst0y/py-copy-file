def copy_file(command: str) -> None:
    list_of_files = command.split(" ")

    if len(list_of_files) == 3:

        command = list_of_files[0]
        file_out = list_of_files[1]
        file_in = list_of_files[2]

        if file_in != file_out and command == "cp":
            with open(file_out, "r") as out, open(file_in, "w") as into:
                for line in out:
                    into.write(line)
