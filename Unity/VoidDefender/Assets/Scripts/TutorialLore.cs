using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class TutorialLore : MonoBehaviour {

	public Text loreBtn;
	public Text tutorialBtn;
	
	public Canvas tutorialCanvas;

	public GameObject tutorialLoreMaster;

	public Button prev;
	public Button next;

	private NavigationPage[] tutorialLoreSelection;

	private int currentTutorialPage;
	private NavigationPageSub[] tutorialPages;

	// Use this for initialization
	void Start ()
	{
		//Gets our tutorial pages
		tutorialLoreSelection = tutorialLoreMaster.GetComponentsInChildren<NavigationPage>(true);
		tutorialPages = tutorialLoreSelection[1].GetComponentsInChildren<NavigationPageSub>(true);
        SetLore();
	}
	
	public void SetLore()
	{
		//make the lore page visible while the tutorial page invisible
		tutorialLoreSelection[0].gameObject.SetActive(true);
		
        loreBtn.GetComponent<Button>().interactable = false;
		
		tutorialLoreSelection[1].gameObject.SetActive(false);
		tutorialBtn.GetComponent<Button>().interactable = true;
	}
	public void SetTutorial()
	{
		currentTutorialPage = 0;
		SetCurrentTutorialPage();

		//make the tutorial page visible while the lore page invisible

		tutorialLoreSelection[0].gameObject.SetActive(false);
		tutorialBtn.GetComponent<Button>().interactable = false;


		tutorialLoreSelection[1].gameObject.SetActive(true);
		loreBtn.GetComponent<Button>().interactable = true;


	}
	void SetCurrentTutorialPage()
	{
		CheckTutorialNavigation();//checks if the next/prev is supposed to be off
								  //Shuts off every page, then activates the one we want.
		for (int i = 0; i< tutorialPages.Length; i++)
		{
			if (i == currentTutorialPage)
			{
				tutorialPages[i].gameObject.SetActive(true);
			}
			else
			{
				tutorialPages[i].gameObject.SetActive(false);
			}
		}
	}
	
	void CheckTutorialNavigation()
	{
		//Uses ternary notation to set whether or not the next or prev is blocked out

		prev.interactable = (currentTutorialPage == 0) ? false : true;
		next.interactable = (currentTutorialPage == tutorialPages.Length - 1) ? false : true;
	}

	public void IncrementTutorialPage()
	{
		currentTutorialPage++;
		SetCurrentTutorialPage();
		CheckTutorialNavigation();
	}
	public void DecrementTutorialPage()
	{
		currentTutorialPage--;
		SetCurrentTutorialPage();
		CheckTutorialNavigation();
	}
}
