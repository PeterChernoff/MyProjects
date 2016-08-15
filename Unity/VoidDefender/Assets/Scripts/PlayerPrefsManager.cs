using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections.Generic;


using System.Collections;

public class PlayerPrefsManager : MonoBehaviour {
	//always use this for manipulating data for player prefs

	public const string MASTER_VOLUME_KEY = "master_volume";
	public const string MASTER_DIFFICULTY_KEY = "difficulty";
	public const string LEVEL_KEY = "level_unlocked_";//we want to have a template to send data
	public const string OPTIONS_KEY = "options";
    const int DEFAULT_OPTIONS_INDEX = 4;//this will be changed if there are any alterations
	

	public static void SetMasterVolume (float volume) {
		if ((volume >= 0f) && (volume <= 1f)) {
			PlayerPrefs.SetFloat(MASTER_VOLUME_KEY, volume);
		} else {
			Debug.LogError("Master volume out of range");
		}

	}
    public static void SetOptionsIndexInitial()
    {
        //Sometimes, we need to have a default number.
        int getOptionsIndex = GetOptionsIndex();
        if (getOptionsIndex != DEFAULT_OPTIONS_INDEX)
        {
            //Makes sure that the index is 4
            PlayerPrefsManager.SetOptionsIndex(DEFAULT_OPTIONS_INDEX);
        }

    }

	public static int GetOptionsIndex()
	{
		return PlayerPrefs.GetInt(OPTIONS_KEY);
	}
	public static void SetOptionsIndex(int optionsLocation)
	{
		if (optionsLocation <= SceneManager.sceneCountInBuildSettings - 1)
		{ //The total number of levels and we start at 0
			PlayerPrefs.SetInt(OPTIONS_KEY, optionsLocation);//We want to set the level we retrieve to be at the options level
		}
		else {
			Debug.LogError("Trying to unlock level not in build order");
		}
	}

	public static float GetMasterVolume() {
		return PlayerPrefs.GetFloat(MASTER_VOLUME_KEY);
	}

	public static void UnlockLevel (int level) {
		if (level <= SceneManager.sceneCountInBuildSettings-1) { //The total number of levels and we start at 0
			PlayerPrefs.SetInt(LEVEL_KEY + level.ToString(), 1);//Use 1 for true, since we don't have booleans
		} else {
			Debug.LogError("Trying to unlock level not in build order");
		}
	}

	public static void LockLevel(int level)
	{
		if (level <= SceneManager.sceneCountInBuildSettings - 1)
		{ //The total number of levels and we start at 0
			PlayerPrefs.SetInt(LEVEL_KEY + level.ToString(), 0);//Use 1 for true, since we don't have booleans
		}
		else {
			Debug.LogError("Trying to lock level not in build order");
		}
	}

	public static bool IsLevelUnlocked(int level) {
		int levelValue = PlayerPrefs.GetInt(LEVEL_KEY + level.ToString());
		bool isLevelUnlocked = (levelValue == 1);
		
		if (level <= SceneManager.sceneCountInBuildSettings - 1)
		{
			return isLevelUnlocked;
		} else {
				Debug.LogError("Trying to check level not in build order");
			return false;
		}
	}


	public static void SetDifficultyLevel(float difficulty)
	{
		if ((difficulty >= 1f) && (difficulty <= 3f))
		{
			PlayerPrefs.SetFloat(MASTER_DIFFICULTY_KEY, difficulty);
		}
		else {
			Debug.LogError("Difficulty out of range");
		}

	}

	public static float GetDifficultyLevel()
	{
		return PlayerPrefs.GetFloat(MASTER_DIFFICULTY_KEY);
	}





}
