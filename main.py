import random
original_balance = 20000
original_bet = 0.10
nbr_turns = 1000
target_multiplier = 1.9  # Ce que tu vises pour gagner
nbr_simulation = 10000

def generate_limbo_result():
    # Résultat Limbo suit une loi exponentielle inversée
    # Source : Stake, BC.Game, etc.
    return 1 / (1 - random.random())  # Simule des résultats comme Limbo

def run_simulation():
    balance = original_balance
    bet = original_bet
    
    for turn in range(nbr_turns):
        if bet > balance:
            #print(f"Tour {turn} : Pas assez de balance pour miser ({bet:.2f}$).")
            break
    
        balance -= bet
        limbo_result = generate_limbo_result()
        #print(f"Tour {turn} | Mise : {bet:.2f}$ | Résultat : {limbo_result:.2f}x | Balance : {balance:.2f}$")
    
        if limbo_result >= target_multiplier:
            gain = bet * target_multiplier
            balance += gain
            #print(f"✅ Gagné ! Gain : {gain:.2f}$ | Nouvelle balance : {balance:.2f}$")
            bet = original_bet  # reset
        else:
            #print(f"❌ Perdu. Nouvelle mise : {bet * 2:.2f}$")
            bet *= 2
    
    #print(f"\nBalance finale après {turn + 1} tours : {balance:.2f}$")
    return balance >= original_balance  # True si win, False si loss
        
# Liste des résultats
results = []

for simulation in range(nbr_simulation):
    result = run_simulation()
    results.append(result)

# Calcul du % de victoires
wins = results.count(True)
losses = results.count(False)
win_percentage = (wins / nbr_simulation) * 100

print(f"Sur {nbr_simulation} simulations :")
print(f"✅ Victoires : {wins} ({win_percentage:.2f}%)")
print(f"❌ Défaites : {losses} ({100 - win_percentage:.2f}%)")