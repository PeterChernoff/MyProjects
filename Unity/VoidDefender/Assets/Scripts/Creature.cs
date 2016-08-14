using UnityEngine;
using System.Collections;

public class Creature : MonoBehaviour {

	//Uses some booleans to keep track of living status
	protected bool isAlive;
	void Start()
	{
		isAlive = true;
	}
	public void SetLife(bool life)
	{
		isAlive = life;
	}
	public bool GetLife()
	{
		return isAlive;
	}
}
