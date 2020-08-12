<?php
    $get = $_GET['email'];
    if (isset($get)) {
        $command = shell_exec('python ./test.py '.$get);
         if($command == "KETEMU ANJING!"){
            echo "live";
         }else{
             echo "die";
         }
    }else{
        echo "param not valid"." example [api.php?email=afiaryaudy@yahoo.com]";
    }
    
?>