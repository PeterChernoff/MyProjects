using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class LevelManager : MonoBehaviour {

	public float autoLoadNextLevel;

	//public MusicManager musicSpawn;
	void Awake()
	{
		//If the game loads for the absolute first time, we want to set the defaults

		if (!PlayerPrefs.HasKey(PlayerPrefsManager.MASTER_VOLUME_KEY)) PlayerPrefsManager.SetMasterVolume(0.5f);
		if (!PlayerPrefs.HasKey(PlayerPrefsManager.MASTER_DIFFICULTY_KEY)) PlayerPrefsManager.SetDifficultyLevel(2);

		//Spawns a music player if we have none
		if (!GameObject.FindGameObjectWithTag("MusicPlayer"))
		{
			GameObject musicSpawn = Instantiate(Resources.Load("Persistent Music Manager")) as GameObject;
		}
		

	}
	void Start()
	{
		if (autoLoadNextLevel > 0)
		{
			Invoke("LoadNextLevel", autoLoadNextLevel);//Invoke will load the method after x seconds
		} /*else {
			//Debug.Log("You are at level " + Application.loadedLevel);
			//Do nothing
			//we'd have an error but we don't care at this point
		}*/
		
		PlayerPrefsManager.UnlockLevel(SceneManager.GetActiveScene().buildIndex);
		//print("Level " + SceneManager.GetActiveScene().buildIndex + " unlocked!");

		/*if (musicSpawn)
		{
			Instantiate(musicSpawn, transform.position, Quaternion.identity);
		}*/
		

	}
	public void CheckLoadLevel(string name)
	{
		//Do something to pause game
		LoadLevel(name);
	}
	public void LoadLevel(string name) {
		//Debug.Log("Level load requested for: " + name);
		SceneManager.LoadScene(name);
		
	}
	
	public void quitGame()
	{
		//Debug.Log("Quitting game");
		Application.Quit();
	}
	public void LoadNextLevel()
	{
		SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);//loadedlevel loads the current level index

	}
}
