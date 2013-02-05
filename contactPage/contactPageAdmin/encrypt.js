/**
 * Encrypts a string using an XOR gate.
 * The ciphertext a sequence of numbers between 0 and 255, seperated by a '-' character. The character 'X' is used as padding to make the number 3 characters.
 * The 'mode' parameter is true for encryption, false for decryption
 * The 'password' parameter is the password used to en/decrypt the string
 * The 'input' paramater is the string to be en/decrypted
 */
var xor = function(mode, password, input) {
	if(password.length==0||input.length==0) return ""; //If there was no input
	password = password.toLowerCase();
	if(mode) {
		if(password.length<(input.length)) {
			var count = 0;
			while(password.length<(input.length)) {
				password += password.charAt(count);
				count++;
				if(count==password.length) {
					count = 0;
				}
			}
		}
	} else {
		if(password.length<(input.length/4)) {
			var count = 0;
			while(password.length<(input.length/4)) {
				password += password.charAt(count);
				count++;
				if(count==password.length) {
					count = 0;
				}
			}
		}
	}
	var outputString = "";
	var cipherChars = input.split("-");
	for (var i=0;i<password.length;i++) {
		if(mode) {
			var toAdd = (password.charCodeAt(i) ^ input.charCodeAt(i));
			outputString += ((i>0) ? "-" : "") + ((toAdd<100) ? ((toAdd<10) ? toAdd + "XX" : toAdd + "X") : toAdd); //To Encrypt
		} else {
			var thisChar = cipherChars[i];
			thisChar = thisChar.replace("X", "");
			outputString += String.fromCharCode(password.charCodeAt(i) ^ parseInt(thisChar, 10));
		}
	}
	return outputString;
}