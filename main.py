from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

    # Questions to collect facts for reasoning
def collect_initial_facts():
    facts = []

    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")

    # Find out budget of the user high, medium, low
    budget = input("Is your budget high, medium, or low? (h/m/l)\n h = high, m = medium, l = low: ").lower()
    if budget.startswith("h"):
        facts.append("budget_high")
    elif budget.startswith("m"):
        facts.append("budget_medium")
    elif budget.startswith("l"):
        facts.append("budget_low")

    if input("Will you be using the laptop for creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is gaming a primary use case? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Will you only use it for office work? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
        
    # Specific Requirements for the laptop
    if input("Do you need a large screen (15 inches or more)? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you need AI acceleration hardware? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")

    # Find OS Preference of the user windows, macos, linux
    # But windows rule is not given in the knowledge base in the rules file
    os_pref = input("Do you prefer Windows, macOS, or Linux? (w/m/l) \n w = Windows, m = macOS, l = Linux : ").lower()
    if os_pref.startswith("m"):
        facts.append("pref_os_macos")
    elif os_pref.startswith("l"):
        facts.append("pref_os_linux")
    return facts

    # In this I have Load rules, create engine, assert facts, and run 
    # inference and print results if no rules fired I have given default 
    # recommendation of basic_laptop
def main():

    
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)

    initial_facts = collect_initial_facts()
    engine.assert_facts(initial_facts)
    engine.run()

    conclusions = engine.conclusions()

    print("\n")
    print("\n")
    if conclusions["recommendations"]:
        for rec in conclusions["recommendations"]:
            print(f"Recommendation: {rec.replace('recommend:', '')}")
            break
    else:
            # This is the default recommendation if no rules fired
            print("Recommendation: basic_laptop")
            print("Explanation: no rule matched — default recommendation chosen.")

    print("\n")

    for step in engine.trace:
        if step["added_fact"].startswith("recommend:"):
            print(f"Explanation: derived from rule '{step['rule']}'")
            break

    print("\n Suggested Specification:")
    for spec in conclusions["specs"]:
        print(f" {spec.replace('spec:', '')}")

    print("\n")
    print("Facts Learned:")
    for fact in conclusions["other_facts"]:
        print(f" {fact}")

if __name__ == "__main__":
    main()
