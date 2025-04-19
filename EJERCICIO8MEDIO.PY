//solción 1

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        resultado = 0
        valor = False
        int_max = 2**31 - 1
        int_min = -2**31
        caracteres = ["+", "-"]
        n = 0

        for x in s:
            if x == " ":
                    pass
            elif x == "0":
                if resultado != 0:
                    resultado *= 10
                elif (n + 1 < len(s)) and (s[n+1] == " "):
                    break
                else:
                    pass  
            elif x in caracteres:
                if n != 0 and ((s[n-1]).isdigit() or (s[n-1]) in caracteres or s[n+1] == " "):
                    break
                else:
                    if x == "-":
                        valor = True
            elif x.isdigit():
                if resultado < 1 and valor:
                    resultado = (resultado * 10) - int(x)   
                else:
                    resultado = (resultado * 10) + int(x)
                
                if (n + 1 < len(s)) and s[n+1] == " ":
                    break
            else:
                break
            n+=1

        if resultado > int_max:
            return int_max
        elif resultado < int_min:
            return int_min
        elif resultado in caracteres:
            return 0
        else:
            return resultado
