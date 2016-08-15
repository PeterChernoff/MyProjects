using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class Tutorial : MonoBehaviour {
	
	public GameObject[] pages;


	public Text next;
	public Text prev;
	private Button nextB;
	private Button prevB;


	private int currentVal;
	// Use this for initialization
	void Start () {
		nextB = next.GetComponent<Button>();
		prevB = prev.GetComponent<Button>();
		currentVal = 0;
		SetPage();
	}

	void SetPage()
	{
		//disables the pages that are not in use and enables the ones that are
		for (int i = 0; i< pages.Length; i++)
		{
			if (i != currentVal)
			{
				pages[i].SetActive(false);
			}
			else
			{
				pages[i].SetActive(true);
			}
		}
	}
	void IncrementPage()
	{
		//go to next page
		if (currentVal < pages.Length)
		{
			currentVal++;
		}
		CheckButtonEnabled();
	}
	void DecrementPage()
	{
		//go to previous page
		if (currentVal > 0)
		{
			currentVal--;
		}
		CheckButtonEnabled();

	}
	void CheckButtonEnabled()
	{
		
		if (currentVal == 0)
		{
			prevB.interactable = false;
		}
		else if (currentVal == pages.Length-1)
		{
			nextB.interactable = false;
		}
		else
		{
			prevB.interactable = true;
			prevB.interactable = true;
		}
	}

}
