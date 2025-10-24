<?php
    /*ORIGINAL CREATOR: darkwall
    AUTHOR: darkwall
    Copyright (C) 2025 darkwall
    License: GNU General Public License v3.0*/ 

    function Decode($content){
        $converted = base64_decode($content);
        $String = utf8_encode($converted);
        return $String;
    }
?>