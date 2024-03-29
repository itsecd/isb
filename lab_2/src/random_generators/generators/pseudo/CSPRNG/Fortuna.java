package random_generators.generators.pseudo.CSPRNG;

import java.nio.ByteBuffer;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.HashMap;

import random_generators.generators.Generator;
import random_generators.generators.pseudo.PRNG.Linear;

public class Fortuna implements Generator
{
    private static final int DEFAULT_COUNT_POOLS = 16;
    private static final int DEFAULT_MAX_COUNT_OUTPUT_BYTE = 64;
    private static final int DEFAULT_COUNT_POOLS_FOR_RANDOM_SEC = 3;
    
    private static final int DEFALUT_COEF_FOR_GENERATOR = 16807;
    private static final int DEFALUT_INCREMENT_FOR_GENERATOR = 0;
    private static final int DEFAULT_MODULUS_FOR_GENERATOR = (int) Math.pow(2, 30);
    private static final int DEFAULT_MODULUS_FOR_GENERATOR_BYTE = 255;


    private byte[] seed;
    private HashMap<Integer, byte[]> pools;
    private final int countMaxPools;

    private int countGenerate;
    private int countUpdatePools;

    
    private Linear genLinear;


    public Fortuna(final String seed) throws Exception
    {
        this(seed.getBytes());
    }
    
    public Fortuna(final byte[] seed) throws Exception
    {
        this(seed, DEFAULT_COUNT_POOLS, DEFAULT_MAX_COUNT_OUTPUT_BYTE);
    }

    public Fortuna(final byte[] seed, final int countPools, final int countBytesInOutput) throws Exception
    {
        if(seed.length > countBytesInOutput) throw new Exception("Размер ключа не должен превышать " + countBytesInOutput + " символов");
        if(countPools < 0) throw new Exception("Количество пулов слишком мало.");
        
        this.seed = new byte[countBytesInOutput];
        
        for(int i = 0; i < seed.length; ++i) this.seed[i] = seed[i]; 
        
        this.countMaxPools = countPools;
        pools = new HashMap<>(countPools);
        countGenerate = 0;
        countUpdatePools = 0;
        this.genLinear = new Linear(ByteBuffer.wrap(this.seed).getInt(), DEFALUT_COEF_FOR_GENERATOR, DEFALUT_INCREMENT_FOR_GENERATOR, DEFAULT_MODULUS_FOR_GENERATOR);
    }
    
    public void updatePool(final Integer idPool, final String poolForMerge)
    {
        updatePool(idPool, poolForMerge.getBytes());
    }
    
    public void updatePool(final Integer idPool, final byte[] poolForMerge)
    {    
        pools.put(idPool % countMaxPools, hashSumArrays(pools.get(idPool), poolForMerge));
    }

    public void updateRandomPool(final String poolForMerge)
    {
        updatePool(generate(), poolForMerge);
    }

    public void updatePools()
    {
        for(Integer idPool : pools.keySet()) 
            if(countUpdatePools % Math.pow(idPool, 2) == 0) pools.put(idPool, hashSumArrays(seed, pools.get(idPool)));
        
        ++countUpdatePools;
    }

    public void updatePools(final int index, final Integer value)
    {
        updatePool(index % countMaxPools, value.toString().getBytes());
        updatePools();
    }

    public void reseed()
    {
        for(byte[] pool : pools.values())
            seed = hashSumArrays(seed, pool);
    }

    private byte[] hashSumArrays(final byte[] firstPool, final byte[] secondPool)
    {
        int sizeResult = 0;

        if(secondPool != null && firstPool != null) sizeResult = Math.max(secondPool.length, firstPool.length);
        else if(secondPool != null) sizeResult = secondPool.length;
        else if(firstPool != null) sizeResult = firstPool.length;

        if(sizeResult > seed.length) sizeResult = seed.length;

        byte[] result = new byte[sizeResult];

        for(int i = 0; i < result.length; ++i)
        {
            if(firstPool != null && i < firstPool.length) result[i] = (byte) (result[i] + firstPool[i] );
            if(secondPool != null && i < secondPool.length) result[i] = (byte) (result[i] + secondPool[i] );
        }

        return result;
    }

    @Override
    public int generate()
    {
        return ByteBuffer.wrap(generateByte()).getInt();
    }
    
    @Override
    public int generate(final int max)
    {
        return Math.abs(generate() % max);
    }
    
    public byte[] generateByte(final int countBytes)
    {
        byte[] result = new byte[countBytes];
        
        for(int i = 0; i < result.length; ++i)
        {
            result[i] =  (byte) (genLinear.generate() % DEFAULT_MODULUS_FOR_GENERATOR_BYTE + seed[i % seed.length]);

            for(byte[] pool : pools.values())
            {
                for(byte pool_el : pool)
                {
                    result[i] += (byte) ((generateByteCommand(seed[i % seed.length], pool_el)));
                    ++countGenerate;
                    if(countGenerate % seed.length == 0) reseed();
                }
            }

            updatePools(i, genLinear.generate());
        }
        return result;
    }

    public byte[] generateByte()
    {
        return generateByte(seed.length);
    }
    
    private byte generateByteCommand(final byte byteFirst, final byte byteSecond)
    {
        switch ((int) (byteFirst + byteSecond) % 7) 
        {
            case 1:
            return (byte) (byteFirst ^ byteSecond);
            case 2:
            return (byte) (byteFirst & byteSecond);
            case 3:
            return (byte) (byteSecond >> 1);
            case 4:
            return (byte) (byteFirst << 1);
            case 5:
            return (byte) (byteFirst << 1);
            case 6:
            return (byte) (byteSecond << 1);
            default:
            return (byte) (byteFirst | byteSecond);
        }
    }

    public byte[] randomSecurityByte()
    {
        for(int i = 0; i < DEFAULT_COUNT_POOLS_FOR_RANDOM_SEC; ++i)
            updatePool(hashSecurity(), Integer.toString(hashSecurity()));
        return generateByte();
    }

    @Override
    public int randomSecurity()
    {
        return ByteBuffer.wrap(randomSecurityByte()).getInt();
    }

    @Override
    public int randomSecurity(final int max)
    {
        return Math.abs(randomSecurity() % max);
    }

    private int hashSecurity()
    {
        return LocalTime.now().getNano() + Runtime.getRuntime().availableProcessors() + LocalDateTime.now().getMinute();
    } 
}