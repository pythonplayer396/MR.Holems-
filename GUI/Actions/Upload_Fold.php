<?php
    /*ORIGINAL CREATOR: darkwall
    AUTHOR: darkwall
    Copyright (C) 2025 darkwall
    License: GNU General Public License v3.0*/

    $filename = "../Graphs/Temp.txt";
    $reader = fopen("../Graphs/TempEncode.txt","r");
    $name = fgets($reader);
    fclose($reader);
    echo move_uploaded_file(
        $_FILES["upFile"]["tmp_name"],
        $name
    )? "OK":"ERROR";
?> 
