import hashlib
import itertools
import string
import time

# ==========================================
# 1. CRIPTOGRAFIA POR SUBSTITUIÇÃO (Cifra de César)
# ==========================================
def cifra_de_cesar(texto, deslocamento, modo='codificar'):
    resultado = ""
    if modo == 'decodificar':
        deslocamento = -deslocamento
        
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            novo_caractere = chr((ord(caractere) - base + deslocamento) % 26 + base)
            resultado += novo_caractere
        else:
            resultado += caractere
    return resultado

# ==========================================
# 2. FUNÇÃO HASH (Com Salt Aprimorado)
# ==========================================
SALT_ALURA = "S3cur1ty_St4rt!"

def gerar_hash_senha(senha):
    # Combinando a senha com o Salt para proteção avançada
    senha_combinada = senha + SALT_ALURA
    return hashlib.sha256(senha_combinada.encode('utf-8')).hexdigest()

# ==========================================
# 3. BANCO DE DADOS E AUTENTICAÇÃO
# ==========================================
banco_usuarios = {
    "aluno_alura": gerar_hash_senha("xyz")  # Senha cadastrada com segurança
}

def realizar_login(usuario, senha_digitada):
    if usuario in banco_usuarios:
        if gerar_hash_senha(senha_digitada) == banco_usuarios[usuario]:
            print(f"🔓 [LOGIN] Acesso concedido! Bem-vindo, {usuario}.")
            return True
    print("❌ [LOGIN] Usuário ou senha incorretos!")
    return False

# ==========================================
# 4. SIMULAÇÃO DE ATAQUE DE FORÇA BRUTA
# ==========================================
def ataque_forca_bruta(hash_alvo, max_letras=3):
    caracteres = string.ascii_lowercase
    tentativas = 0
    inicio = time.time()
    
    print("\n[!] Iniciando simulação de ataque de força bruta...")
    
    for tamanho in range(1, max_letras + 1):
        for combinacao in itertools.product(caracteres, repeat=tamanho):
            tentativas += 1
            senha_teste = "".join(combinacao)
            hash_teste = gerar_hash_senha(senha_teste)
            
            if hash_teste == hash_alvo:
                fim = time.time()
                print(f"💥 SENHA QUEBRADA! A senha secreta é: '{senha_teste}'")
                print(f"📊 Tentativas necessárias: {tentativas}")
                print(f"⏱️ Tempo gasto: {fim - inicio:.4f} segundos")
                return senha_teste
                
    print("❌ O ataque falhou. A senha é complexa demais para o limite atual.")
    return None

# ==========================================
# EXECUÇÃO DO PROJETO
# ==========================================
if __name__ == "__main__":
    print("--- 🛡️ ALURA SECURITY LAB 🛡️ ---")
    
    # Testando Cifra
    msg = "Seguranca da Informacao Alura 2026"
    codificado = cifra_de_cesar(msg, 7, 'codificar')
    print(f"\n🔑 [Cifra] Texto Protegido: {codificado}")
    print(f"🔑 [Cifra] Texto Decifrado: {cifra_de_cesar(codificado, 7, 'decodificar')}")
    
    # Testando Login
    print()
    realizar_login("aluno_alura", "senha_errada")
    if realizar_login("aluno_alura", "xyz"):
        # Testando Força Bruta contra a nossa própria senha cadastrada
        hash_alvo = banco_usuarios["aluno_alura"]
        ataque_forca_bruta(hash_alvo, max_letras=3)
