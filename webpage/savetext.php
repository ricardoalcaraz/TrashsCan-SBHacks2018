<?php
		$data = $_POST['barcode'];
		$ret = file_put_contents('barcodes.csv', $data.",", FILE_APPEND | LOCK_EX);
		if($ret === false) {
			echo "$data";
			die('There was an error writing');
		}
		else {
			header("Location: {$_SERVER['HTTP_REFERER']}");
			exit;
		}
?>
