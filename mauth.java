class auth
{
 
    
    static int session_a = 17;
    static int session_b = 20;
 
    static String encrypt_store_android(char[] msg)
    {
        
        String cipher = "";
        for (int i = 0; i < msg.length; i++)
        {
          
            if (msg[i] != ' ')
            {
                cipher = cipher
                        + (char) ((((session_a * (msg[i] - 'A')) + session_b) % 26) + 'A');
            } else 
            {
                cipher += msg[i];
            }
        }
        return cipher;
    }
 
    static String decrypt_validation_android(String cipher)
    {
        String msg = "";
        int a_inv = 0;
        int flag = 0;
 
        
        for (int i = 0; i < 26; i++)
        {
            flag = (session_a * i) % 26;
 
            
            if (flag == 1)
            {
                a_inv = i;
            }
        }
        for (int i = 0; i < cipher.length(); i++)
        {
            
            if (cipher.charAt(i) != ' ')
            {
                msg = msg + (char) (((a_inv *
                        ((cipher.charAt(i) + 'A' - session_b)) % 26)) + 'A');
            }
            else 
            {
                msg += cipher.charAt(i);
            }
        }
 
        return msg;
    }
 
   
    public static void main(String[] args)
    {
        String username = "abcabc@gmail.com";
        String pwd="abcabc";
        String msg = "AFFINE CIPHER";
 
        
        String cipherText = encrypt_store_android(pwd.toUpperCase().toCharArray());
        System.out.println("Encrypted Message is : " + cipherText);
 
        
        System.out.println("Decrypted Message is: " + decrypt_validation_android(cipherText).toLowerCase());
 
    }
}
