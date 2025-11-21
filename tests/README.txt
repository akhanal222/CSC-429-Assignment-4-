Test Case 1 — Premium Ultrabook
--------------------------------------------------------------------------------------
Input Facts portable, long_battery, budget_high

Expected Recommendation: premium_ultrabook

Expected Rule Fired: Premium Ultrabook

Expected Specs: (none)

--------------------------------------------------------------------------------------

Test Case 2 — Budget Office Ultrabook
--------------------------------------------------------------------------------------

Input Facts: portable, budget_low, office_only

Expected Recommendation: budget_ultrabook

Expected Rule Fired: Student light office

Expected Specs: (none)

Expected Other Facts: portable, budget_low, office_only




--------------------------------------------------------------------------------------
Test Case 3 — Midrange Gaming Laptop
--------------------------------------------------------------------------------------

Input Facts: portable, budget_low, office_only

Expected Recommendation: budget_ultrabook

Expected Rule Fired: Student light office

Expected Specs: (none)

Expected Other Facts: portable, budget_low, office_only




--------------------------------------------------------------------------------------

Test Case 4 — High-End Gaming Laptop
--------------------------------------------------------------------------------------

Input Facts: gaming, budget_high

Expected Recommendation: high_end_gaming_laptop

Expected Rule Fired: Pro gaming

Expected Specs: (none)

Expected Other Facts: gaming, budget_high





--------------------------------------------------------------------------------------

Test Case 5 — Creative Work (Portable + Large Screen)
--------------------------------------------------------------------------------------

Input Facts: creative_work, portable, large_screen

Expected Recommendation: default recommendation chosen(basic_laptop)

Expected Rules Fired: Creative work (portable), Creative work (display)

Expected Specs: ram_16_plus, display_15_plus_color_accurate

Expected Other Facts: creative_work, portable, large_screen




--------------------------------------------------------------------------------------
Test Case 6 — AI Acceleration Laptop
--------------------------------------------------------------------------------------

Input Facts: needs_ai_accel

Expected Recommendation: default recommendation chosen(basic_laptop)

Expected Rule Fired: AI acceleration

Expected Specs: gpu_with_tensor_cores

Expected Other Facts: needs_ai_accel




--------------------------------------------------------------------------------------

Test Case 7 — Linux + Office Work
--------------------------------------------------------------------------------------

Input Facts: pref_os_linux, office_only

Expected Recommendation: default recommendation chosen(basic_laptop)

Expected Rule Fired: Linux suitability

Expected Specs: linux_friendly_hw

Expected Other Facts: pref_os_linux, office_only

