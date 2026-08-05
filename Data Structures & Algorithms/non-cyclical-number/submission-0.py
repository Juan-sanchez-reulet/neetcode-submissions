class Solution:
    def isHappy(self, n: int) -> bool:
        # Conjunto para guardar los números que ya hemos calculado
        vistos = set()
        
        # El bucle continúa mientras no lleguemos a 1 y no haya un ciclo
        while n != 1 and n not in vistos:
            # Marcamos el número actual como visto
            vistos.add(n)
            
            # Calculamos la suma de los cuadrados de sus dígitos
            n = self.sum_of_squares(n)
            
        # Si salimos del bucle porque n == 1, devuelve True.
        # Si salimos porque 'n in vistos', devuelve False.
        return n == 1

    def sum_of_squares(self, n: int) -> int:
        suma = 0
        for digito in str(n):
            suma += int(digito) ** 2
        return suma