def calculate_rice_grains_in_idli():
    print("Idli Rice Grain Calculator")

    idli_weight_grams = float(input("Enter idli weight in grams: "))
    rice_ratio = float(input("Enter rice ratio in the batter : "))
    rice_grain_weight_grams = float(
        input("enter the average weight of one rice grain : "))

    rice_weight_gram = idli_weight_grams * rice_ratio
    grains_of_rice = rice_weight_gram / rice_grain_weight_grams

    print(f"\nApproximate grains of rice in one idli: {int(grains_of_rice)}")


calculate_rice_grains_in_idli()
