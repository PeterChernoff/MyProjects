using UnityEngine;
using System.Collections;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

[RequireComponent(typeof(Text))]
public class LevelCheck : MonoBehaviour
{

	private Text theText;
	private Button theButton;
	// Use this for initialization
	void Start()
	{
		theButton = GetComponent<Button>();
		theText = gameObject.GetComponent<Text>();//Gets the text in game object
		//print(theText.text);
		int levelIndex = int.Parse(theText.text);//converts it to an int
		int level = levelIndex + PlayerPrefsManager.GetOptionsIndex();

		//print(name + " " + level + ", Options is at " + PlayerPrefsManager.GetOptionsIndex());
		if (PlayerPrefsManager.IsLevelUnlocked(level))
		{
			theButton.interactable = true;
		}
	}

}
