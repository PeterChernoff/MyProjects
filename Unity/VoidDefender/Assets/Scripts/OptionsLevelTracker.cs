using UnityEngine;
using UnityEngine.SceneManagement;

using System.Collections;

public class OptionsLevelTracker : MonoBehaviour {

	//we want to be able to get where Options is in the build, because it's the last value before we get to the game proper. It will help us keep track of what levels are unlocked
	
	private static int optionsIndex;
	// Use this for initialization
	void Awake () {
		optionsIndex = SceneManager.GetActiveScene().buildIndex;
        //print(optionsIndex);

        PlayerPrefsManager.SetOptionsIndex(optionsIndex);

	}
}
