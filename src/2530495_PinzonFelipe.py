# Manejo de strings en Python

## Nombre: Felipe Pinzon Segura
## Marticula: 2530495
## Grupo: IM 1-2

# Resumen Ejecutivo
"""
    Un string en Python es una secuencia inmutable de caracteres, lo que significa que
    cualquier operación de modificación (como reemplazar o concatenar) resulta en la
    creación de una nueva cadena, manteniendo la original intacta. Las operaciones
    básicas incluyen obtener su longitud con len(), concatenar con el operador +,
    extraer sub-cadenas mediante slicing (e.g., text[a:b]), y buscar patrones con
    el operador 'in' o el método find(). Es crucial validar y normalizar el texto de
    entrada (usando strip(), lower(), etc.) antes de su procesamiento, ya que esto
    previene errores, asegura consistencia en las comparaciones y protege contra
    datos basura, vital para entradas como correos electrónicos o contraseñas.
    Este documento cubre seis problemas prácticos que demuestran el uso de métodos
    de string esenciales, aplicando validaciones rigurosas y documentando la lógica
    con descripciones, entradas, salidas y casos de prueba concretos para cada solución.
"""

# Principles & Good Practices (short list)
"""
    - Inmutabilidad: Entender que los strings son inmutables; cualquier "cambio"
    crea una nueva instancia de la cadena.
    - Normalización: Es fundamental normalizar la entrada de usuario con strip()
    (para eliminar espacios iniciales/finales) y lower() o upper() (para
    comparaciones sin distinción de mayúsculas/minúsculas).
    - Claridad en Slicing: Evitar "números mágicos" en índices; documentar o usar
    variables para explicar qué rango de caracteres se está extrayendo.
    - Uso de Métodos: Preferir los métodos incorporados de string (como split(),
    replace(), title()) en lugar de implementar lógica básica desde cero.
    - Diseño de Validaciones: Las validaciones deben ser claras: primero verificar
    que la entrada no esté vacía y luego comprobar el formato (si aplica).
    - Legibilidad: Usar nombres de variables descriptivos (lower_snake_case) y
    mensajes de error explícitos en inglés.
"""


# Problem 1: Full name formatter (name + initials)
"""
# Description: Formats a person's full name to Title Case and extracts initials.

# Inputs:
- full_name (string): complete name possibly with extra spaces and mixed case

# Outputs:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

# Validations:
- full_name must not be empty after strip()
- Must contain at least two words
- Cannot be only spaces

# Test cases:
1) Normal: "felipe pinzon segura" → "Felipe Pinzon Segura", "F.P.S."
2) Border: "  FELIPE PINZON  " → "Felipe Pinzon", "F.P."
3) Error: "" → Error message
"""

full_name = input("Enter full name: ").strip()
    
# Validaciones
if not full_name:
    print("Error: Name cannot be empty")
    exit()
    
name_parts = full_name.split()
    
if len(name_parts) < 2:
    print("Error: Name must contain at least two words")      
    exit()
    
# Formatear nombre en Title Case
formatted_name = ' '.join(part.title() for part in name_parts)
    
# Extraer iniciales
initials = '.'.join(part[0].upper() for part in name_parts) + '.'
    
print(f"Formatted name: {formatted_name}")
print(f"Initials: {initials}")


# Problem 2: Simple email validator (structure + domain)
"""
Description: Validates email format and extracts domain if valid.

Inputs:
- email_text (string): email address to validate

Outputs:
- "Valid email: true" or "Valid email: false"
- If valid: "Domain: <domain_part>"

Validations:
- email_text must not be empty after strip()
- Must contain exactly one '@'
- Must contain at least one '.' after '@'
- Cannot contain spaces

Test cases:
1) Normal: "user@example.com" → true, "example.com"
2) Border: "user@sub.domain.com" → true, "sub.domain.com"  
3) Error: "invalid.email" → false
"""
email_text = input("Enter email: ").strip()
    
# Validaciones
if not email_text:
    print("Valid email: false")
    exit()
      
if ' ' in email_text:
    print("Valid email: false")
    exit()
      
at_count = email_text.count('@')
    
if at_count != 1:
    print("Valid email: false")
    exit()
    
at_position = email_text.find('@')
domain_part = email_text[at_position + 1:]
    
if '.' not in domain_part or domain_part.startswith('.'):
    print("Valid email: false")
    exit()
    
# Si pasa todas las validaciones, el email es válido
print("Valid email: true")
print(f"Domain: {domain_part}")


# Problem 3: Palindrome checker (ignoring spaces and case)
""" 
Description: Checks if a phrase is a palindrome ignoring case and spaces.

Inputs:
- phrase (string): text to check for palindrome

Outputs:
- "Is palindrome: true" or "Is palindrome: false"
- "Normalized: <cleaned_phrase>"

Validations:
- phrase must not be empty after strip()
- Minimum length of 3 characters after cleaning

Test cases:
1) Normal: "Amolapaloma" → true
2) Border: "o" → false (too short after cleaning)
3) Error: "   " → Error message
"""
phrase = input("Enter phrase: ").strip()
    
# Validaciones
if not phrase:
    print("Error: Phrase cannot be empty")
    exit()
       
# Normalizar: convertir a minúsculas y eliminar espacios
normalized = phrase.lower().replace(' ', '')
    
if len(normalized) < 3:
    print("Error: Phrase too short after normalization")
    exit()
    
# Determinar si es palíndromo
is_palindrome = normalized == normalized[::-1]
    
# Mostrar resultados
print(f"Is palindrome: {str(is_palindrome).lower()}")
print(f"Normalized: {normalized}")


# Problem 4: Sentence word stats (lengths and first/last word)
"""
Description: Analyzes word statistics in a sentence.

Inputs:
- sentence (string): text to analyze

Outputs:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>" 
- "Shortest word: <...>"
- "Longest word: <...>"

Validations:
- sentence must not be empty after strip()
- Must contain at least one valid word

Test cases:
1) Normal: "The game pokemon za" → count:4, first:"The", last:"za", shortest:"za", longest:"pokemon"
2) Border: "Pikachu" → count:1, first/last:"Hello", shortest/longest:"Hello"
3) Error: "   " → Error message
"""
sentence = input("Enter sentence: ").strip()
    
# Validaciones
if not sentence:
    print("Error: Sentence cannot be empty")
    exit()
    
words = sentence.split()
    
if not words:
    print("Error: No valid words found")
    exit()
    
# Calcular estadísticas
word_count = len(words)
first_word = words[0]
last_word = words[-1]

# Encontrar palabras más corta y más larga
shortest_word = min(words, key=len)
longest_word = max(words, key=len)
    
# Mostrar resultados
print(f"Word count: {word_count}")
print(f"First word: {first_word}")
print(f"Last word: {last_word}")
print(f"Shortest word: {shortest_word}")
print(f"Longest word: {longest_word}")


# Problem 5: Password strength classifier
"""
Description: Classifies password strength as weak, medium, or strong.

Inputs:
- password_input (string): password to evaluate

Outputs:
- "Password strength: weak"
- "Password strength: medium" 
- "Password strength: strong"

Validations:
- password_input must not be empty

Strength rules:
- Weak: length < 8 OR all lowercase letters only
- Medium: length >= 8 AND (mix of upper/lower case OR contains digits)
- Strong: length >= 8 AND has uppercase, lowercase, digit, and symbol

Test cases:
1) Normal: "Pokefan123!" → strong
2) Border: "Xyz330" → weak (length < 8)
3) Error: "" → Error message
"""
password_input = input("Enter password: ").strip()
    
# Validación: no aceptar contraseña vacía
if not password_input:
    print("Error: Password cannot be empty")
    exit()
    
# Verificar características
has_upper = any(c.isupper() for c in password_input)
has_lower = any(c.islower() for c in password_input) 
has_digit = any(c.isdigit() for c in password_input)
has_symbol = any(not c.isalnum() for c in password_input)
    
length = len(password_input)
    
# Clasificar fortaleza según reglas:
# - Weak: longitud < 8 o solo minúsculas sin otros tipos de caracteres
# - Strong: longitud >= 8 y contiene mayúsculas, minúsculas, dígitos y símbolos
# - Medium: cualquier otro caso (longitud >= 8 con alguna combinación de tipos)
if length < 8 or (has_lower and not has_upper and not has_digit and not has_symbol):
    strength = "weak"
elif has_upper and has_lower and has_digit and has_symbol and length >= 8:
    strength = "strong"
else:
    strength = "medium"
    
print(f"Password strength: {strength}")


# Problem 6: Product label formatter (fixed-width text)
"""
Description: Creates a fixed-width product label exactly 30 characters long.

Inputs:
- product_name (string): name of product
- price_value (string): price (will be converted to number)

Outputs:
- "Label: '<exactly 30 characters>'"

Validations:
- product_name must not be empty after strip()
- price_value must be convertible to positive number

Test cases:
1) Normal: "Coffee", "2.50" → "Product: Coffee | Price: $2.50       "
2) Border: "Very long product name here", "99.99" → truncated to 30 chars
3) Error: "", "abc" → Error messages
"""
product_name = input("Enter product name: ").strip()
price_input = input("Enter price: ").strip()

# Validaciones
if not product_name:
    print("Error: Product name cannot be empty")
    exit()
    
try:
    price_value = float(price_input)
    if price_value <= 0:
        print("Error: Price must be positive")
        exit()
except ValueError:
    print("Error: Invalid price format")
    exit()

# Create base label
base_label = f"Product: {product_name} | Price: ${price_value:.2f}"

# Ensure exactly 30 characters
if len(base_label) > 30:
    formatted_label = base_label[:30]
else:
    formatted_label = base_label.ljust(30)

print(f"Label: '{formatted_label}'")


# CONCLUSIONES
"""
    El manejo de strings es la base de la interacción I/O en casi cualquier programa.
    Es esencial para formatear la salida al usuario y, críticamente, para procesar
    cualquier tipo de dato textual de entrada. La normalización con lower(), upper()
    y strip() es vital antes de cualquier comparación o validación para eliminar
    ambigüedades (e.g., " User " vs "user").
    
    El uso de métodos de string como split() y join() facilita la manipulación de palabras, 
    mientras que el slicing (text[::-1]) demuestra el poder de la sintaxis concisa
    de Python para la inversión de cadenas. Finalmente, la inmutabilidad de los strings,
    aunque genera nuevas instancias en cada cambio, garantiza que las cadenas originales
    no se corrompan inesperadamente, lo cual es clave para escribir código robusto y predecible.
"""

# REFERENCIAS
"""
    1) Python documentation - Built-in Types: Text Sequence Type — str.
       URL: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    2) W3Schools Python String Methods.
       URL: https://www.w3schools.com/python/python_ref_string.asp
    3) GeeksforGeeks - Python String Slicing.
       URL: https://www.geeksforgeeks.org/python-string-slicing/
    4) Real Python - Palindromes in Python.
       URL: https://realpython.com/python-palindromes/
    5) IBM Developer - Best practices for data validation.
       URL: https://developer.ibm.com/articles/data-validation-best-practices/
"""

# REPOSITORIO DE GITHUB
"""
    URL: https://github.com/FelipePinzonS/Manejo_De_Strings.git
"""