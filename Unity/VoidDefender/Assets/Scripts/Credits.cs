using UnityEngine;
using UnityEngine.UI;

using System.Collections;


public class Credits : MonoBehaviour {
	private GameObject pagesController;
	private Text myText;
	private Button prev, next;
	private int currentPage;
	private NavigationPage[] pages;

	

	// Use this for initialization
	void Start ()
	{
		//For some reason, the buttons weren't being registered in the public values
		prev = GameObject.Find("Prev").GetComponent<Button>();
		next = GameObject.Find("Next").GetComponent<Button>();

		currentPage = 0;
		pagesController = GameObject.Find("Pages");

		pages = pagesController.GetComponentsInChildren<NavigationPage>(true);

		/*foreach (NavigationPage page in pages)
		{
			print(page.name);
		}*/
		DisplayCredits();

		CheckButtons();

	}

	public void DisplayCredits()
	{
		//Gives us the current credits page
		CheckButtons();

		for (int i = 0; i < pages.Length; i++)
		{
			if (i == currentPage)
			{
				pages[i].gameObject.SetActive(true);
			}
			else
			{
				pages[i].gameObject.SetActive(false);
			}
		}
	}
	void CheckButtons()
	{
		//disables the buttons if we're at the ends
		if (currentPage >= pages.Length-1)
		{
			next.interactable = false;
		}
		else
		{
			next.interactable = true;
		}

		if (currentPage == 0)
		{
			prev.interactable = false;
		}
		else
		{
			prev.interactable = true;
		}
		//print(currentPage);

	}
	public void Increment()
	{
		//changes the page we're on
		if (currentPage < pages.Length)
		{
			currentPage++;
		}
		DisplayCredits();
	}
	public void Decrement()
	{
		//changes the page we're on
		if (currentPage > 0)
		{
			currentPage--;
		}
		DisplayCredits();
	}
	public void GoToWebPage(string webPage)
	{
		Application.OpenURL(webPage);
	}

}
