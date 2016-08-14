using UnityEngine;
using System.Collections;
using System.Linq;
using UnityEngine.SceneManagement;

public class MusicManager : MonoBehaviour {

	private static MusicManager instance = null;
	public AudioClip[] levelMusicPreGame;
	public AudioClip[] levelMusicGame;
	public AudioClip[] levelMusicPostGame;

	public AudioClip[] levelMusicChangeArray;
	private AudioSource audioSource;

	// Use this for initialization
	void Awake () {
		//We want this to be persistent
		if (instance != null)
		{
			Destroy(gameObject); //if there are duplicates, kill self
			//Debug.Log("Extra Music Player destroyed");
		}
		else {
			instance = this;
			GameObject.DontDestroyOnLoad(gameObject);
			//SceneManager.activeSceneChanged += OnLevelWasLoadedDelegate; //Unity keeps complaining

		}

		SetupMusic();
		audioSource = GetComponent<AudioSource>();

	}
	void Start(){
        PlayerPrefsManager.SetOptionsIndexInitial();

		audioSource.volume = PlayerPrefsManager.GetMasterVolume();//sets the sound
		OnLevelWasLoaded(SceneManager.GetActiveScene().buildIndex);


	}
	void SetupMusic()
	{
		//we want music for each level.

		//The total music array size is the setup levels, + the levels + the ending levels
		levelMusicChangeArray = new AudioClip[levelMusicPreGame.Length + levelMusicGame.Length + levelMusicPostGame.Length];

		int setupMusic = 0;

		//Get the music for the setup levels
		for (int i = 0; i < levelMusicPreGame.Length; i++)
		{
			AddMusicToArray(levelMusicPreGame[i], setupMusic);
			setupMusic++;
		}

		//Get the music for the game levels
		for (int i = 0; i < levelMusicGame.Length; i++)
		{
			AddMusicToArray(levelMusicGame[i], setupMusic);
			setupMusic++;
		}

		//Get the music for the game over screens
		for (int i = 0; i < levelMusicPostGame.Length; i++)
		{
			AddMusicToArray(levelMusicPostGame[i], setupMusic);
			setupMusic++;
		}

	}
	void AddMusicToArray(AudioClip audioToAdd, int whereToAdd)
	{
		//adds music to the main array
		levelMusicChangeArray[whereToAdd] = audioToAdd;
	}
	public void ChangeVolume(float volume) {
		//sets the volume
		audioSource.volume = volume;
	}
	
	void OnLevelWasLoaded(int level)
	{
		AudioClip thisLevelMusic = levelMusicChangeArray[level];

		if (thisLevelMusic) { //if there is music attached
			audioSource.enabled = true;
			audioSource.clip = thisLevelMusic;

			audioSource.loop = true;
			audioSource.Play();
		}
	}

    void SpecialCheck()
    {

    }
}
