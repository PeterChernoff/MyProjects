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
		//standard adding energy
		starDisplay.AddDarkEnergy(starsToAdd);

	}
	public void AddStars(int amount)
	{
		//adding energy from animator
		starDisplay.AddDarkEnergy(amount);
	}

}
