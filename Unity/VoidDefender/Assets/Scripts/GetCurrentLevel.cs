using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;
using UnityEngine.UI;

public class GetCurrentLevel : MonoBehaviour {

	private Text text;

	// Use this for initialization
	void Start () {
		
		//we want the text to tell us what level we're on
		text = GameObject.FindGameObjectWithTag("LevelDisplay").GetComponent<Text>() as Text;
		//This could be more efficient, but this is for clarity
		int sceneIndex = SceneManager.GetActiveScene().buildIndex;
		//print("Index level " + sceneIndex);
		int lastPreGameIndex = PlayerPrefsManager.GetOptionsIndex();
		//print("Pregame level " + lastPreGameIndex);

		int currentLevel;
		//Allows me to use a sample level more easily
		if (sceneIndex > SceneManager.sceneCountInBuildSettings)
		{
			currentLevel = 7;
		}
		else
		{
			currentLevel = sceneIndex - lastPreGameIndex;
		}
			
		text.text = "Level 0" + currentLevel;
	}
	
}
