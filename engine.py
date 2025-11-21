from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """ Return True if all antecedents are true and consequent not yet known."""
        # pass
        return all(a in self.facts for a in rule.antecedents) and rule.consequent not in self.facts

    def run(self) -> None:
        """The run method implements the forward chaining algorithm. It continues to loop as long as there are rules that can fire.
           In each iteration, it checks all the rules sorted by priority (highest first). and if a rule can fire, it adds its consequent to the facts.
        """
        fire = True
    
        while fire:
            fire = False
            for rule in sorted(self.rules, key=lambda r: r.priority, reverse=True):
                if self.can_fire(rule):
                    self.facts.add(rule.consequent) 
                    self.trace.append({
                        "rule": rule.name,
                        "added_fact": rule.consequent
                    })
                    fire = True
                    break

    def conclusions(self) -> Dict[str, List[str]]:
        """Return separated results (recommendations, specs, other facts)."""
        recommendations = []
        specs = []
        other_facts = []
        for fact in self.facts:
            if fact.startswith("recommend:"):
                recommendations.append(fact)
            elif fact.startswith("spec:"):
                specs.append(fact)
            else:
                other_facts.append(fact)
        return {
            "recommendations": recommendations,
            "specs": specs,
            "other_facts": other_facts
        }