from generate_data import fetch_valid_data
from analyzer import load_data, clean_data, perform_analysis, calculate_stability_score

# This is the 'Main Controller' script. It tells everything else 
# when to start and what to do.

def main():
    print("**************************************************")
    print("    WELCOME TO THE CAREER STABILITY ANALYZER      ")
    print("**************************************************\n")

    # Step 1: Get the raw data from the internet
    input_file = fetch_valid_data()
    if not input_file:
        print("Couldn't get the data. Please check your internet connection!")
        return

    # Step 2: Load and Clean the data
    # (We don't want any 'NaN' or empty spots ruining our math)
    df = load_data(input_file)
    df = clean_data(df)

    # Step 3: Run the numbers
    # We'll see which major categories are the current salary kings
    perform_analysis(df)

    # Step 4: Calculate our custom 'Stability Score'
    # This ranks majors from 'Highly Secure' to 'Volatile'
    final_df = calculate_stability_score(df)

    # Step 5: Print out some cool findings
    print("\n" + "*"*50)
    print("             KEY MARKET FINDINGS                  ")
    print("*"*50)

    # Find the major with the absolute highest stability score
    best_row = final_df.loc[final_df['Stability_Score'].idxmax()]
    print(f">> Top Pick: '{best_row['Major']}' is the most stable major right now.")
    print(f"   Score: {best_row['Stability_Score']}/100")

    # Count how many majors are actually 'Highly Secure'
    secure_count = len(final_df[final_df['Status'] == 'Highly Secure'])
    print(f">> Market Check: There are {secure_count} majors classified as 'Highly Secure'.")

    # Step 6: Save our hard work to a new file
    output_path = "data/final_career_results.csv"
    final_df.to_csv(output_path, index=False)
    
    print(f"\n[DONE] All results saved to: {output_path}")
    print("**************************************************")

if __name__ == "__main__":
    main()
