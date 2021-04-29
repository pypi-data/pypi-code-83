"""
GHS Hazard pictogram data
"""

GHS_HAZARDS = [
    {
        'code': 'GHS01',
        'name': 'Explosive',
        'hazard_type': 'Physical',
        'usage': """
            - Unstable explosives
            - Explosives, divisions 1.1, 1.2, 1.3, 1.4, 1.5, 1.6
            - Self-reactive substances and mixtures, types A, B
            - Organic peroxides, types A, B
        """,
        'example': 'azidoazide azide, TNT, chromyl chloride, nitroglycerin',
        'pictogram': 'ghs02.svg'
    },
    {
        'code': 'GHS02',
        'name': 'Flammable',
        'hazard_type': 'Physical',
        'usage': """
            - Flammable gases, category 1
            - Flammable aerosols, categories 1, 2
            - Flammable liquids, categories 1, 2, 3, 4
            - Flammable solids, categories 1, 2
            - Self-reactive substances and mixtures, types B, C, D, E, F
            - Pyrophoric liquids, category 1
            - Pyrophoric solids, category 1
            - Combustible solids, category 3
            - Combustible liquids, category 3
            - Self-heating substances and mixtures, categories 1, 2
            - Substances and mixtures, which in contact with water,
            - emit flammable gases, categories 1, 2, 3'
            - Organic peroxides, types B, C, D, E, F
        """,
        'example': 'acetone, methanol, generally most solvents.',
        'pictogram': 'ghs02.svg'
    },
    {
        'code': 'GHS03',
        'name': 'Oxidizing',
        'hazard_type': 'Physical',
        'usage': """
            - Oxidizing gases, category 1
            - Oxidizing liquids, categories 1, 2, 3
            - Oxidizing solids, categories 1, 2, 3
        """,
        'example': 'sulfur dioxide, most halogens, '
                   'potassium permanganate, nitric acid ',
        'pictogram': 'ghs03.svg'
    },
    {
        'code': 'GHS04',
        'name': 'Compressed Gas',
        'hazard_type': 'Physical',
        'usage': """
            - Compressed gases
            - Liquefied gases
            - Refrigerated liquefied gases
            - Dissolved gases
        """,
        'example': 'liquid nitrogen, liquid oxygen, liquid helium',
        'pictogram': 'ghs04.svg'
    },
    {
        'code': 'GHS05',
        'name': 'Compressed Gas',
        'hazard_type': 'Physical',
        'usage': """
            - Corrosive to metals, category 1
            - Explosives, divisions 1.5, 1.6
            - Flammable gases, category 2
            - Self-reactive substances and mixtures
            - type G (see HAZMAT Class 4 Flammable solids)
            - Organic peroxides, type G
            - Skin corrosion, categories 1A, 1B, 1C
            - Serious eye damage, category 1
        """,
        'usage_exclusion': """
            - Explosives, divisions 1.5, 1.6
            - Flammable gases, category 2
            - Self-reactive substances and mixtures, type G (see HAZMAT Class 4 Flammable solids)
            - Organic peroxides, type G
        """,
        'example': 'Strong acids/bases (nitric acid, sodium hydroxide), '
                   'calcium oxide, anhydrous zinc chloride can be corrosive ',
        'pictogram': 'ghs05.svg'
    },
    {
        'code': 'GHS06',
        'name': 'Toxic',
        'hazard_type': 'Health',
        'usage': """
            Acute toxicity (oral, dermal, inhalation), categories 1, 2, 3
        """,
        'example': 'Manganese Heptoxide '
                   '(fire diamond rating at health hazard is 4)',
        'pictogram': 'ghs06.svg'
    },
    {
        'code': 'GHS07',
        'name': 'Harmful',
        'hazard_type': 'Health',
        'usage': """
            - Acute toxicity (oral, dermal, inhalation), category 4
            - Skin irritation, categories 2, 3
            - Eye irritation, category 2A
            - Skin sensitization, category 1
            - Specific target organ toxicity following single exposure, category 3
              - Respiratory tract irritation
              - Narcotic effects
        """,
        'usage_exclusion': """
            Not used
            - with the "skull and crossbones" pictogram
            - for skin or eye irritation '
              - if the "corrosion" pictogram also appears
              - if the "health hazard" pictogram is used to indicate respiratory sensitization
        """,
        'example': '',
        'pictogram': 'ghs07.svg'
    },
    {
        'code': 'GHS08',
        'name': 'Health hazard',
        'hazard_type': 'Health',
        'usage': """
            - Respiratory sensitization, category 1
            - Germ cell mutagenicity, categories 1A, 1B, 2
            - Carcinogenicity, categories 1A, 1B, 2
            - Reproductive toxicity, categories 1A, 1B, 2
            - Specific target organ toxicity following single exposure, categories 1, 2
            - Specific target organ toxicity following repeated exposure'categories 1, 2
            - Aspiration hazard, categories 1, 2
        """,
        'usage_exclusion': """
            - Acute toxicity (oral, dermal, inhalation), category 5
            - Eye irritation, category 2B
            - Reproductive toxicity – effects on or via lactation
        """,
        'example': 'Chromium',
        'pictogram': 'ghs08.svg'
    },
    {
        'code': 'GHS09',
        'name': 'Environmental hazard',
        'hazard_type': 'Health',
        'usage': """
            - Acute hazards to the aquatic environment, category 1
            - Chronic hazards to the aquatic environment, categories 1, 2 
            - Environmental toxicity, categories 1, 2
        """,
        'usage_exclusion': """
            - Acute hazards to the aquatic environment, categories 2, 3
            - Chronic hazards to the aquatic environment, categories 3, 4
        """,
        'example': 'Manganese Heptoxide '
                   '(fire diamond rating at health hazard is 4)',
        'pictogram': 'ghs09.svg'
    },
    {
        'code': 'Division1.1',
        'name': 'Division 1.1',
        'hazard_type': 'Transport - Class 1 - Explosives',
        'usage': """
            Explosives - Substances and articles which have a mass explosion hazard
        """,
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division11.svg'
    },
    {
        'code': 'Division1.2',
        'name': 'Division 1.2',
        'hazard_type': 'Transport - Class 1 - Explosives',
        'usage': """
            Explosives - Substances and articles which have a projection hazard but not a mass explosion hazard
        """,
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division12.svg'
    },
    {
        'code': 'Division1.3',
        'name': 'Division 1.3',
        'hazard_type': 'Transport - Class 1 - Explosives',
        'usage': """
            Explosives - Substances and articles which have a fire hazard and either a minor blast hazard or a minor projection hazard or both, but not a mass explosion hazard
        """,
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division13.svg'
    },
    {
        'code': 'Division1.4',
        'name': 'Division 1.4',
        'hazard_type': 'Transport - Class 1 - Explosives',
        'usage': """
            Explosives - Substances and articles which are classified as explosives but which present no significant hazard
        """,
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division14.svg'
    },
    {
        'code': 'Division1.5',
        'name': 'Division 1.5',
        'hazard_type': 'Transport - Class 1 - Explosives',
        'usage': "Explosives - Very insensitive substances which have a mass explosion hazard",
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division15.svg'
    },
    {
        'code': 'Division1.6',
        'name': 'Division 1.6',
        'hazard_type': 'Transport - Class 1 - Explosives',
        'usage': "Explosives - No hazard statement",
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division16.svg'
    },
    {
        'code': 'Division2.1',
        'name': 'Division 2.1',
        'hazard_type': 'Transport - Class 2 - Gases',
        'usage': """
            Flammable gases – Gases which at 20 °C and a standard pressure of 101.3 kPa: 
            - are ignitable when in a mixture of 13 percent or less by volume with air; or
            - have a flammable range with air of at least 12 percentage points regardless of the lower flammable limit.
        """,
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division21.svg'
    },
    {
        'code': 'Division2.2',
        'name': 'Division 2.2',
        'hazard_type': 'Transport - Class 2 - Gases',
        'usage': """
            Non-flammable non-toxic gases – Gases: 
            - which are asphyxiant – gases which dilute or replace the oxygen normally in the atmosphere; or
            - are oxidizing – gases which may, generally by providing oxygen, cause or contribute to the combustion of other material more than air does; or
            - do not come under the other divisions.
            """,
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division22.svg'
    },
    {
        'code': 'Division2.3',
        'name': 'Division 2.3',
        'hazard_type': 'Transport - Class 2 - Gases',
        'usage': """
            Toxic gases – Gases which:
            - are known to be so toxic or corrosive to humans as to pose a hazard to health; or
            - are presumed to be toxic or corrosive to humans because they have an LC50 value equal to or less than 5000 ml/m3 (ppm).
        """,
        'note': 'The asterisks are replaced by '
                'the class number and compatibility code',
        'pictogram': 'division23.svg'
    },
    {
        'code': 'Class3',
        'name': 'Class 3',
        'hazard_type': 'Transport - Classes 3 and 4 - Flammable liquids and solids',
        'usage': """
            Flammable liquids – Liquids which have a flash point of less than 60 °C and which are capable of sustaining combustion 
        """,
        'pictogram': 'class3.svg'
    },
    {
        'code': 'Division4.1',
        'name': 'Division 4.1',
        'hazard_type': 'Transport - Classes 3 and 4 - Flammable liquids and solids',
        'usage': """
            Flammable solids, self-reactive substances and solid desensitized explosives – Solids which, under conditions encountered in transport, are readily combustible or may cause or contribute to fire through friction; self-reactive substances which are liable to undergo a strongly exothermic reaction; solid desensitized explosives which may explode if not diluted sufficiently  
        """,
        'pictogram': 'division41.svg'
    },
    {
        'code': 'Division4.2',
        'name': 'Division 4.2',
        'hazard_type': 'Transport - Classes 3 and 4 - Flammable liquids and solids',
        'usage': """
            Substances liable to spontaneous combustion – Substances which are liable to spontaneous heating under normal conditions encountered in transport, or to heating up in contact with air, and being then liable to catch fire   
        """,
        'example': 'e.g. manganese heptoxide',
        'pictogram': 'division42.svg'
    },
    {
        'code': 'Division4.3',
        'name': 'Division 4.3',
        'hazard_type': 'Transport - Classes 3 and 4 - Flammable liquids and solids',
        'usage': """
            Substances which in contact with water emit flammable gases – Substances which, by interaction with water, are liable to become spontaneously flammable or to give off flammable gases in dangerous quantities
        """,
        'pictogram': 'division43.svg'
    },
    {
        'code': 'Division5.1',
        'name': 'Division 5.1',
        'hazard_type': 'Transport - Other GHS transport classes',
        'usage': """
            Oxidizing substances – Substances which, while in themselves not necessarily combustible, may, generally by yielding oxygen, cause, or contribute to, the combustion of other material 
        """,
        'pictogram': 'division51.svg'
    },
    {
        'code': 'Division5.2',
        'name': 'Division 5.2',
        'hazard_type': 'Transport - Other GHS transport classes',
        'usage': """
            Toxic substances – Substances with an LD50 value ≤ 300 mg/kg (oral) or ≤ 1000 mg/kg (dermal) or an LC50 value ≤ 4000 ml/m3 (inhalation of dusts or mists) 
        """,
        'pictogram': 'division52.svg'
    },
    {
        'code': 'Division6.1',
        'name': 'Division 6.1',
        'hazard_type': 'Transport - Other GHS transport classes',
        'usage': """
            Organic peroxides – Organic substances which contain the bivalent –O–O– structure and may be considered derivatives of hydrogen peroxide, where one or both of the hydrogen atoms have been replaced by organic radicals
        """,
        'example': 'nearly everything that contains cyanide groups ',
        'pictogram': 'division61.svg'
    },
    {
        'code': 'Class6.2',
        'name': 'Class 6.2',
        'hazard_type': 'Non-GHS transport',
        'usage': """
            Infectious substances
        """,
        'pictogram': 'class62.svg'
    },
    {
        'code': 'Class7a',
        'name': 'Class 7a',
        'hazard_type': 'Non-GHS transport',
        'usage': """
            Radioactive material I
         """,
        'pictogram': 'class7a.svg'
    },
    {
        'code': 'Class7b',
        'name': 'Class 7b',
        'hazard_type': 'Non-GHS transport',
        'usage': """
            Radioactive material II
         """,
        'pictogram': 'class7b.svg'
    },
    {
        'code': 'Class7c',
        'name': 'Class 7c',
        'hazard_type': 'Non-GHS transport',
        'usage': """
            Radioactive material III
         """,
        'pictogram': 'class7c.svg'
    },
    {
        'code': 'Class7e',
        'name': 'Class 7e',
        'hazard_type': 'Non-GHS transport',
        'usage': """
            Radioactive material - Fissile
         """,
        'pictogram': 'class7e.svg'
    },
    {
        'code': 'Class8',
        'name': 'Class 8',
        'hazard_type': 'Transport - Other GHS transport classes',
        'usage': """
            Corrosive substances – Substances which:
            - cause full thickness destruction of intact skin tissue on exposure time of less than 4 hours; or
            - exhibit a corrosion rate of more than 6.25 mm per year on either steel or aluminium surfaces at 55 °C
        """,
        'pictogram': 'class8.svg'
    },
    {
        'code': 'Class9',
        'name': 'Class 9',
        'hazard_type': 'Non-GHS transport',
        'usage': """
            Miscellaneous dangerous substances and articles 
        """,
        'pictogram': 'class9.svg'
    },
]
