using UnityEngine;
using System.Collections;

public class Altar : MonoBehaviour {
	private DarkEnergyDisplay starDisplay;
	private int starsToAdd = 15;//lets us adjust how much energy we get
	void Start()
	{

		starDisplay = GameObject.FindObjectOfType<DarkEnergyDisplay>();
	}
	public void AddStarsManual()
	{

		starDisplay.AddDarkEnergy(starsToAdd);

	}
	public void AddStars(int amount)
	{
		starDisplay.AddDarkEnergy(amount);
	}

}
