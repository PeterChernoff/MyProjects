using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System.Collections;

public class OptionsController : MonoBehaviour
{
	public Slider volumeSlider, difficultySlider;
	public LevelManager levelManager;
	public Text difficultyExplanation;
	public GameObject[] enemyDisplay;

	private string[] textExplanation = {
		"More starting Dark Energy, weaker enemies.",
		"Standard starting Dark Energy, standard enemies.",
		"Less starting Dark Energy, stronger enemies.",
	};

	private MusicManager musicManager;
	private bool notCheckedMusic = true;

	private float sliderMin;
	private float sliderMax;
	// Use this for initialization
	void Start () {
		musicManager = GameObject.FindObjectOfType<MusicManager>();
		volumeSlider.value = PlayerPrefsManager.GetMasterVolume();//set the slider to the new value
		difficultySlider.value = PlayerPrefsManager.GetDifficultyLevel();//set the slider to the new value
		sliderMin = difficultySlider.minValue;
		sliderMax = difficultySlider.maxValue;

		DisplayEnemies();

	}

	
	// Update is called once per frame
	void Update ()
	{
		//Changes the music when we slide
		//musicManager.ChangeVolume(volumeSlider.value);
		
	}
	public void OptionsChangeVolume()
	{
		musicManager.ChangeVolume(volumeSlider.value);
	}
	public void DisplayEnemies()
	{
		//show off the extra enemies to represent difficulty
		for (int i = 0; i < enemyDisplay.Length; i++)
		{
			if (i+sliderMin <= difficultySlider.value)
			{
				enemyDisplay[i].SetActive(true);
			}
			else
			{
				enemyDisplay[i].SetActive(false);
			}
		}
		difficultyExplanation.text = textExplanation[(int)difficultySlider.value-1];
	}
	public void SaveAndExit()
	{
		PlayerPrefsManager.SetMasterVolume(volumeSlider.value);
		PlayerPrefsManager.SetDifficultyLevel(difficultySlider.value);

		levelManager.LoadLevel("L01a_Start");
	}
	public void SetDefaults()
	{
		PlayerPrefsManager.SetMasterVolume(0.5f);
		PlayerPrefsManager.SetDifficultyLevel(2f);

		volumeSlider.value = PlayerPrefsManager.GetMasterVolume();//set the slider to the new value
		difficultySlider.value = PlayerPrefsManager.GetDifficultyLevel();//set the slider to the new value
	}
	public void Reset()
	{
		//we'll want the options menu to always be the last scene before we load levels
		//We'll want the last two scenes to be the levels we load
		//L01z_Options will be the last pregame level
		for (int i = SceneManager.GetActiveScene().buildIndex - 1;  i<SceneManager.sceneCountInBuildSettings; i++)
		{
			PlayerPrefsManager.LockLevel(i);
		}
	}
}
