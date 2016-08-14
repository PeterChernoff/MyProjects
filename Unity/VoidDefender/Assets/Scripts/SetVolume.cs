using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class SetVolume : MonoBehaviour {

	private MusicManager musicManager;

	// Use this for initialization
	void Start () {
		musicManager = GameObject.FindObjectOfType< MusicManager> ();
		if (musicManager)
		{
			float volume = PlayerPrefsManager.GetMasterVolume();
			musicManager.ChangeVolume(volume);
		}
		else
		{
			Debug.LogWarning("No music manager found");
		}

		//ToDelete();
	}
	void ToDelete()
	{
		print(SceneManager.sceneCountInBuildSettings);
		for (int i = 0; i< SceneManager.sceneCountInBuildSettings; i++)
		{
			print("Level " + i + " unlocked? " + PlayerPrefsManager.IsLevelUnlocked(i));
		}
	}
	
}
