using UnityEngine;
using System.Collections;
using UnityEngine.UI;

[RequireComponent (typeof(Text))]

public class DarkEnergyDisplay : MonoBehaviour {
	public int darkEnergy;
	private Text starText;
	private const int START_DARKENERGY = 100;
	private const int EASY = 25;
	private const int MEDIUM = 0;
	private const int HARD = -10;
	private int difficultyDarkEnergy;
	private int checkDifficulty;

	public enum Status { SUCCESS, FAILURE};
	// Use this for initialization
	void Start () {

		//This assumes we have a difficulty of 1-3
		checkDifficulty = (int)PlayerPrefsManager.GetDifficultyLevel();
		if (checkDifficulty == 1) { difficultyDarkEnergy = EASY; }
		else if (checkDifficulty == 3) { difficultyDarkEnergy = HARD; }
		else { difficultyDarkEnergy = MEDIUM; }//defaults to medium

		darkEnergy = START_DARKENERGY + difficultyDarkEnergy;//adds or deletes dark energy based on difficulty
		starText = GetComponent<Text>();
		UpdateText();
	}

	public void AddDarkEnergy(int amount)
	{
		darkEnergy += amount;
		UpdateText();
	}
	public Status UseDarkEnergy(int amount)
	{
		//Places Defender if we have enough energy
		if (amount > darkEnergy)
		{
			return Status.FAILURE;
		}
		darkEnergy -= amount;
		UpdateText();
		return Status.SUCCESS;
	}
	private void UpdateText()
	{
		starText.text = darkEnergy.ToString();

	}
}
